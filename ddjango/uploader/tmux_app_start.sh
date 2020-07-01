#!/bin/bash/bin
# tmux new -s work -d
tmux rename-window -t work central
tmux send-keys -t work 'cd ~/projects/aviso/analytics-server' C-m
tmux send-keys -t work 'pyenv activate analenv' C-m
tmux send-keys -t work './go runserver' C-m
tmux split-window -h -t work
tmux send-keys -t work 'cd ~/projects/aviso/analytics-server' C-m


tmux new-window -t work
tmux rename-window -t work frontend
tmux send-keys -t work 'cd ~/projects/aviso/analytics-server/welcome/static/js' C-m
tmux send-keys -t work 'nvm use 8.17.0' C-m
tmux send-keys -t work 'node napp.js' C-m

tmux split-window -v -t work
tmux send-keys -t work 'cd ~/projects/aviso/analytics-server/welcome/' C-m
tmux send-keys -t work 'nvm use 8.17.0' C-m
tmux send-keys -t work 'npm run dev-hot' C-m
tmux attach -t work
