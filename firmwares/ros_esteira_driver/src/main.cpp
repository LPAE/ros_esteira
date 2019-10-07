#include <avr/io.h>
#include <ros.h>
#include <std_msgs/Int8.h>

#define USE_USBCON

ros::NodeHandle  nh;
	
//---------------------------------------
#define ENA1 PB0
#define IN11 PB1
#define IN12 PB2
#define ENB1 PB3
#define IN13 PB4
#define IN14 PB5

#define ENA2 PC0
#define IN21 PC1
#define IN22 PC2
#define ENB2 PC3
#define IN23 PC4
#define IN24 PC5

#define IN31 PD0
#define IN32 PD1
#define IN33 PD2
#define IN34 PD3
#define IN35 PD4
#define IN36 PD5
#define IN37 PD6
#define IN38 PD7

//---------------------------------------
std_msgs::Int8 dutycycle_L_cmd, dutycycle_R_cmd;
int8_t dutycycle_L, spin_L, dutycycle_R, spin_R;
std_msgs::Int8 feedback_L, feedback_R;

ros::Publisher pub_feedback_L("driver_feedback_L", &feedback_L);
void dutycycle_L_callback(const std_msgs::Int8 &dutycycle_L_cmd)
{
    dutycycle_L = dutycycle_L_cmd.data;
    if(dutycycle_L < 0){
      dutycycle_L = (-1)*dutycycle_L; 
      spin_L = 0xff;
    }
    else{
      spin_L = 0x00;
    }
    // feedback_L.data = dutycycle_L;
    // pub_feedback_L.publish(&feedback_L);
}
ros::Subscriber<std_msgs::Int8> sub_command_L("driver_L_command", &dutycycle_L_callback);

ros::Publisher pub_feedback_R("driver_feedback_R", &feedback_R);
void dutycycle_R_callback(const std_msgs::Int8 &dutycycle_R_cmd)
{
    dutycycle_R = dutycycle_R_cmd.data;
    if(dutycycle_R < 0){
      dutycycle_R = (-1)*dutycycle_R;
      spin_R = 0xff;
    }
    else{
      spin_R = 0x00;
    }
    // feedback_R.data = dutycycle_R;
    // pub_feedback_R.publish(&feedback_R);
}
ros::Subscriber<std_msgs::Int8> sub_command_R("driver_R_command", &dutycycle_R_callback);

//---------------------------------------
void setup()
{
    dutycycle_L = 0;
    dutycycle_R = 0;

    DDRB = 0xFF;
    DDRC = 0xFF;
    DDRD = 0xFF;

    PCMSK2 = 0x00;
    UCSR0B = 0x00;

    PORTB = 0x00;
    PORTC = 0x00;
    PORTD = 0x00;
  
    nh.initNode();
    nh.subscribe(sub_command_L); nh.subscribe(sub_command_R);
    nh.advertise(pub_feedback_L); nh.advertise(pub_feedback_R);
}

void loop()
{
    for(uint8_t i=0; i < 128; i++)
    {     
      //---------------------------------------
      if(i > dutycycle_L){
        PORTC = 0x00;
      }
      else{
        if(spin_R){
          PORTC = 0b00101101;
          PORTD = 0x00;
        }
        else{
          PORTC = 0b00011011;
          PORTD = 0xFF;
        }         
      }
      //---------------------------------------
      if(i > dutycycle_R){
        PORTB = 0x00;      
      }
      else{
        if(spin_L){
          PORTB = 0b00101101;
          PORTD = 0x00;
        }
        else{
          PORTB = 0b00011011;
          PORTD = 0xFF;
        }        
      }
      //---------------------------------------
      nh.spinOnce(); 
    }   	
}