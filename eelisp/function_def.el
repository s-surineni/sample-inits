;; The following takes a number as input and multiplies it with 7
(defun multiply-by-7 (number)
  "The function multiplies input by 7"
  (* 7 number))

(multiply-by-7 3)


(defun interactive-multiply-by-7 (number)
     "The function multiplies input by 7 interactively"
     (interactive "p")
     ;; this prints the value of variable
     (message "the value of number is %s " number)
     (message "The result is %d" (* 7 number)))

(interactive-multiply-by-7 3)
