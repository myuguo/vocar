// Generated by gencpp from file chip_bldc_driver/Feedback.msg
// DO NOT EDIT!


#ifndef CHIP_BLDC_DRIVER_MESSAGE_FEEDBACK_H
#define CHIP_BLDC_DRIVER_MESSAGE_FEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace chip_bldc_driver
{
template <class ContainerAllocator>
struct Feedback_
{
  typedef Feedback_<ContainerAllocator> Type;

  Feedback_()
    : header()
    , feedback_counter(0)
    , motor_encoder_counter(0)
    , motor_rpm_feedback(0)  {
    }
  Feedback_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , feedback_counter(0)
    , motor_encoder_counter(0)
    , motor_rpm_feedback(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _feedback_counter_type;
  _feedback_counter_type feedback_counter;

   typedef int32_t _motor_encoder_counter_type;
  _motor_encoder_counter_type motor_encoder_counter;

   typedef int32_t _motor_rpm_feedback_type;
  _motor_rpm_feedback_type motor_rpm_feedback;





  typedef boost::shared_ptr< ::chip_bldc_driver::Feedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::chip_bldc_driver::Feedback_<ContainerAllocator> const> ConstPtr;

}; // struct Feedback_

typedef ::chip_bldc_driver::Feedback_<std::allocator<void> > Feedback;

typedef boost::shared_ptr< ::chip_bldc_driver::Feedback > FeedbackPtr;
typedef boost::shared_ptr< ::chip_bldc_driver::Feedback const> FeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::chip_bldc_driver::Feedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::chip_bldc_driver::Feedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::chip_bldc_driver::Feedback_<ContainerAllocator1> & lhs, const ::chip_bldc_driver::Feedback_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.feedback_counter == rhs.feedback_counter &&
    lhs.motor_encoder_counter == rhs.motor_encoder_counter &&
    lhs.motor_rpm_feedback == rhs.motor_rpm_feedback;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::chip_bldc_driver::Feedback_<ContainerAllocator1> & lhs, const ::chip_bldc_driver::Feedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace chip_bldc_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::chip_bldc_driver::Feedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::chip_bldc_driver::Feedback_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::chip_bldc_driver::Feedback_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3cd2728375779c5e385ddf941da8bc30";
  }

  static const char* value(const ::chip_bldc_driver::Feedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3cd2728375779c5eULL;
  static const uint64_t static_value2 = 0x385ddf941da8bc30ULL;
};

template<class ContainerAllocator>
struct DataType< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "chip_bldc_driver/Feedback";
  }

  static const char* value(const ::chip_bldc_driver::Feedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# 20Hz feedback message\n"
"Header header\n"
"\n"
"int32 feedback_counter\n"
"int32 motor_encoder_counter\n"
"int32 motor_rpm_feedback\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
;
  }

  static const char* value(const ::chip_bldc_driver::Feedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.feedback_counter);
      stream.next(m.motor_encoder_counter);
      stream.next(m.motor_rpm_feedback);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Feedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::chip_bldc_driver::Feedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::chip_bldc_driver::Feedback_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "feedback_counter: ";
    Printer<int32_t>::stream(s, indent + "  ", v.feedback_counter);
    s << indent << "motor_encoder_counter: ";
    Printer<int32_t>::stream(s, indent + "  ", v.motor_encoder_counter);
    s << indent << "motor_rpm_feedback: ";
    Printer<int32_t>::stream(s, indent + "  ", v.motor_rpm_feedback);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CHIP_BLDC_DRIVER_MESSAGE_FEEDBACK_H
