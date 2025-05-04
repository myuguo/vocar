cmake_minimum_required(VERSION 2.8.3)
project(chip_bldc_driver)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  serial
  std_msgs
  message_generation
)

## Declare message files to be built
add_message_files(
  FILES
  Command.msg
  Feedback.msg
  Status.msg
  Config.msg
)

## Generate added messages
generate_messages(
  DEPENDENCIES
  std_msgs
)

## Declare the catkin package
catkin_package(
  CATKIN_DEPENDS roscpp serial std_msgs message_runtime
)

## Include directories
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

## Libraries
add_library(bldc_controller src/bldc_controller.cpp)
add_dependencies(bldc_controller chip_bldc_driver_generate_messages_cpp ${catkin_EXPORTED_TARGETS})
target_link_libraries(bldc_controller ${catkin_LIBRARIES})

add_library(bldc_serial src/bldc_serial.cpp)
add_dependencies(bldc_serial chip_bldc_driver_generate_messages_cpp ${catkin_EXPORTED_TARGETS})
target_link_libraries(bldc_serial ${catkin_LIBRARIES})

add_library(crc16 src/crc16.cpp)
add_dependencies(crc16 chip_bldc_driver_generate_messages_cpp ${catkin_EXPORTED_TARGETS})
target_link_libraries(crc16 ${catkin_LIBRARIES})

## Executable
add_executable(bldc_driver_node src/bldc_driver_node.cpp)
add_dependencies(bldc_driver_node chip_bldc_driver_generate_messages_cpp ${catkin_EXPORTED_TARGETS})
target_link_libraries(bldc_driver_node
  bldc_controller
  bldc_serial
  crc16
  ${catkin_LIBRARIES}
)
set_target_properties(bldc_driver_node PROPERTIES OUTPUT_NAME bldc_driver_node PREFIX "")

## Install
install(TARGETS bldc_driver_node bldc_controller bldc_serial crc16
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
)

# If more folders like config, add below
# install(DIRECTORY launch
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
