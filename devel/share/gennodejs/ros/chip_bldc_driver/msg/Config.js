// Auto-generated. Do not edit!

// (in-package chip_bldc_driver.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Config {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.param_code = null;
      this.param_value = null;
    }
    else {
      if (initObj.hasOwnProperty('param_code')) {
        this.param_code = initObj.param_code
      }
      else {
        this.param_code = '';
      }
      if (initObj.hasOwnProperty('param_value')) {
        this.param_value = initObj.param_value
      }
      else {
        this.param_value = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Config
    // Serialize message field [param_code]
    bufferOffset = _serializer.string(obj.param_code, buffer, bufferOffset);
    // Serialize message field [param_value]
    bufferOffset = _serializer.int32(obj.param_value, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Config
    let len;
    let data = new Config(null);
    // Deserialize message field [param_code]
    data.param_code = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [param_value]
    data.param_value = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.param_code);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'chip_bldc_driver/Config';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '25b7fe1b3fe79fec5128554212d66983';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string param_code    # e.g., "MAC", "MDEC", "MAMP", etc.
    int32 param_value    # The value to set
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Config(null);
    if (msg.param_code !== undefined) {
      resolved.param_code = msg.param_code;
    }
    else {
      resolved.param_code = ''
    }

    if (msg.param_value !== undefined) {
      resolved.param_value = msg.param_value;
    }
    else {
      resolved.param_value = 0
    }

    return resolved;
    }
};

module.exports = Config;
