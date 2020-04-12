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


(setq settings-files ("1" "2"))
(defun get-settings-file ()

  (interactive "P")
  (let ((settings-file
         (completing-read "Use this file for loading: "
                          settings-files))
        )
    (settings-file)))


(print (get-settings-file))


(setq settings-files ("1" "2"))
(defun get-settings-file ()

  (interactive "P")
  (let ((settings-file
         (read-file-name "Use this file for loading: "
                         ))
        )
    settings-file))


(print (get-settings-file))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(setq settings-files '("~/ironman/myemacs/init.el" "2"))

(defun get-settings-file ()

  (interactive "P")
  (let ((settings-file
         (completing-read "Use this file for loading: "
                          settings-files))
        )
    settings-file))


(load-file (get-settings-file))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(setq settings-files '("~/ironman/myemacs/init.el"
                       "/Users/sampathsurineni/ironman/prelude/init.el"
                       "/Users/sampathsurineni/ironman/emacs.d/init.el"
                       "/Users/sampathsurineni/ironman/emacs_starter/spacemacs/init.el"))

(defun get-settings-file ()

  (interactive "P")
  (let ((settings-file
         (completing-read "Use this file for loading: "
                          settings-files))
        )
    settings-file))

(defun set-settings-file ()
  (let ((settings-file
         (get-settings-file)))
    (setq user-emacs-directory (file-name-directory settings-file))
    (load-file settings-file)
    )
  )
;; (load-file (get-settings-file))
(set-settings-file)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
