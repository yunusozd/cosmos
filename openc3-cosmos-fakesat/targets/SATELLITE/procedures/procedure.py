# Script Runner test script
cmd("SATELLITE EXAMPLE")
wait_check("SATELLITE STATUS BOOL == 'FALSE'", 5)