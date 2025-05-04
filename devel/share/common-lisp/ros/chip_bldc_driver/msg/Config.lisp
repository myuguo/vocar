; Auto-generated. Do not edit!


(cl:in-package chip_bldc_driver-msg)


;//! \htmlinclude Config.msg.html

(cl:defclass <Config> (roslisp-msg-protocol:ros-message)
  ((param_code
    :reader param_code
    :initarg :param_code
    :type cl:string
    :initform "")
   (param_value
    :reader param_value
    :initarg :param_value
    :type cl:integer
    :initform 0))
)

(cl:defclass Config (<Config>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Config>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Config)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name chip_bldc_driver-msg:<Config> is deprecated: use chip_bldc_driver-msg:Config instead.")))

(cl:ensure-generic-function 'param_code-val :lambda-list '(m))
(cl:defmethod param_code-val ((m <Config>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader chip_bldc_driver-msg:param_code-val is deprecated.  Use chip_bldc_driver-msg:param_code instead.")
  (param_code m))

(cl:ensure-generic-function 'param_value-val :lambda-list '(m))
(cl:defmethod param_value-val ((m <Config>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader chip_bldc_driver-msg:param_value-val is deprecated.  Use chip_bldc_driver-msg:param_value instead.")
  (param_value m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Config>) ostream)
  "Serializes a message object of type '<Config>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'param_code))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'param_code))
  (cl:let* ((signed (cl:slot-value msg 'param_value)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Config>) istream)
  "Deserializes a message object of type '<Config>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'param_code) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'param_code) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'param_value) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Config>)))
  "Returns string type for a message object of type '<Config>"
  "chip_bldc_driver/Config")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Config)))
  "Returns string type for a message object of type 'Config"
  "chip_bldc_driver/Config")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Config>)))
  "Returns md5sum for a message object of type '<Config>"
  "25b7fe1b3fe79fec5128554212d66983")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Config)))
  "Returns md5sum for a message object of type 'Config"
  "25b7fe1b3fe79fec5128554212d66983")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Config>)))
  "Returns full string definition for message of type '<Config>"
  (cl:format cl:nil "string param_code    # e.g., \"MAC\", \"MDEC\", \"MAMP\", etc.~%int32 param_value    # The value to set~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Config)))
  "Returns full string definition for message of type 'Config"
  (cl:format cl:nil "string param_code    # e.g., \"MAC\", \"MDEC\", \"MAMP\", etc.~%int32 param_value    # The value to set~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Config>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'param_code))
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Config>))
  "Converts a ROS message object to a list"
  (cl:list 'Config
    (cl:cons ':param_code (param_code msg))
    (cl:cons ':param_value (param_value msg))
))
