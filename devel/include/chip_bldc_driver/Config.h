// Generated by gencpp from file chip_bldc_driver/Config.msg
// DO NOT EDIT!


#ifndef CHIP_BLDC_DRIVER_MESSAGE_CONFIG_H
#define CHIP_BLDC_DRIVER_MESSAGE_CONFIG_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace chip_bldc_driver
{
template <class ContainerAllocator>
struct Config_
{
  typedef Config_<ContainerAllocator> Type;

  Config_()
    : param_code()
    , param_value(0)  {
    }
  Config_(const ContainerAllocator& _alloc)
    : param_code(_alloc)
    , param_value(0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _param_code_type;
  _param_code_type param_code;

   typedef int32_t _param_value_type;
  _param_value_type param_value;





  typedef boost::shared_ptr< ::chip_bldc_driver::Config_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::chip_bldc_driver::Config_<ContainerAllocator> const> ConstPtr;

}; // struct Config_

typedef ::chip_bldc_driver::Config_<std::allocator<void> > Config;

typedef boost::shared_ptr< ::chip_bldc_driver::Config > ConfigPtr;
typedef boost::shared_ptr< ::chip_bldc_driver::Config const> ConfigConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::chip_bldc_driver::Config_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::chip_bldc_driver::Config_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::chip_bldc_driver::Config_<ContainerAllocator1> & lhs, const ::chip_bldc_driver::Config_<ContainerAllocator2> & rhs)
{
  return lhs.param_code == rhs.param_code &&
    lhs.param_value == rhs.param_value;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::chip_bldc_driver::Config_<ContainerAllocator1> & lhs, const ::chip_bldc_driver::Config_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace chip_bldc_driver

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::chip_bldc_driver::Config_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::chip_bldc_driver::Config_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::chip_bldc_driver::Config_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::chip_bldc_driver::Config_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::chip_bldc_driver::Config_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::chip_bldc_driver::Config_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::chip_bldc_driver::Config_<ContainerAllocator> >
{
  static const char* value()
  {
    return "25b7fe1b3fe79fec5128554212d66983";
  }

  static const char* value(const ::chip_bldc_driver::Config_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x25b7fe1b3fe79fecULL;
  static const uint64_t static_value2 = 0x5128554212d66983ULL;
};

template<class ContainerAllocator>
struct DataType< ::chip_bldc_driver::Config_<ContainerAllocator> >
{
  static const char* value()
  {
    return "chip_bldc_driver/Config";
  }

  static const char* value(const ::chip_bldc_driver::Config_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::chip_bldc_driver::Config_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string param_code    # e.g., \"MAC\", \"MDEC\", \"MAMP\", etc.\n"
"int32 param_value    # The value to set\n"
;
  }

  static const char* value(const ::chip_bldc_driver::Config_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::chip_bldc_driver::Config_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.param_code);
      stream.next(m.param_value);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Config_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::chip_bldc_driver::Config_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::chip_bldc_driver::Config_<ContainerAllocator>& v)
  {
    s << indent << "param_code: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.param_code);
    s << indent << "param_value: ";
    Printer<int32_t>::stream(s, indent + "  ", v.param_value);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CHIP_BLDC_DRIVER_MESSAGE_CONFIG_H
