;; Auto-generated. Do not edit!


(when (boundp 'chip_bldc_driver::Config)
  (if (not (find-package "CHIP_BLDC_DRIVER"))
    (make-package "CHIP_BLDC_DRIVER"))
  (shadow 'Config (find-package "CHIP_BLDC_DRIVER")))
(unless (find-package "CHIP_BLDC_DRIVER::CONFIG")
  (make-package "CHIP_BLDC_DRIVER::CONFIG"))

(in-package "ROS")
;;//! \htmlinclude Config.msg.html


(defclass chip_bldc_driver::Config
  :super ros::object
  :slots (_param_code _param_value ))

(defmethod chip_bldc_driver::Config
  (:init
   (&key
    ((:param_code __param_code) "")
    ((:param_value __param_value) 0)
    )
   (send-super :init)
   (setq _param_code (string __param_code))
   (setq _param_value (round __param_value))
   self)
  (:param_code
   (&optional __param_code)
   (if __param_code (setq _param_code __param_code)) _param_code)
  (:param_value
   (&optional __param_value)
   (if __param_value (setq _param_value __param_value)) _param_value)
  (:serialization-length
   ()
   (+
    ;; string _param_code
    4 (length _param_code)
    ;; int32 _param_value
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _param_code
       (write-long (length _param_code) s) (princ _param_code s)
     ;; int32 _param_value
       (write-long _param_value s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _param_code
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _param_code (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int32 _param_value
     (setq _param_value (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get chip_bldc_driver::Config :md5sum-) "25b7fe1b3fe79fec5128554212d66983")
(setf (get chip_bldc_driver::Config :datatype-) "chip_bldc_driver/Config")
(setf (get chip_bldc_driver::Config :definition-)
      "string param_code    # e.g., \"MAC\", \"MDEC\", \"MAMP\", etc.
int32 param_value    # The value to set

")



(provide :chip_bldc_driver/Config "25b7fe1b3fe79fec5128554212d66983")


