# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs

ORACLE_HOME=/usr/lib/oracle/18.3/client64

PATH=$PATH:$HOME/.local/bin:$HOME/bin:$HOME/MCC/bin:$ORACLE_HOME/bin

export PATH
export LD_LIBRARY_PATH=$ORACLE_HOME/lib
export TNS_ADMIN=$ORACLE_HOME/network/admin
export PATH
export ORACLE_HOME


