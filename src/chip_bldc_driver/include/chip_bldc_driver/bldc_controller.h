#ifndef bldc_controller_H
#define bldc_controller_H

#include "ros/ros.h"
#include "chip_bldc_driver/bldc_serial.h"
#include "chip_bldc_driver/Command.h"
#include "chip_bldc_driver/Config.h"

namespace bldc_controller
{

/**
 * Class implementing bldc controller
 */
class BldcController
{
public:
  BldcController(bldc_serial::BldcSerial *s);
  ~BldcController();
  
private:
  bldc_serial::BldcSerial *serial;
  ros::Timer timeout_timer_;
  ros::Subscriber sub_cmd_, sub_config_;
  ros::NodeHandle nh_;
  void motorCommand(const chip_bldc_driver::Command& command);
  void motorConfig(const chip_bldc_driver::Config& config);
  void timeoutCallback(const ros::TimerEvent&);
 
};

}  // namespace bldc

#endif  // bldc
