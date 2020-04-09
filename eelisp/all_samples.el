(defun select-config-file()
  ;; (interactive)
  (message "Please enter the filename you want to load")
  (read-file-name "vallavalla"))

(print (select-config-file))


(defun ff ()
  "Prompt user to enter a file name, with completion and history support."
  (interactive)
  (message "String is %s" (read-file-name "Enter file name:")))

(ff)
