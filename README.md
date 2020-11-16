
=> Exception shows the time period store or charing station is working or not. 
That's why :
    => If exception is "open" then one can directly look at the end of the exception if the timestamp entered by user is inside this exception. 
    => If exception is "closed" 
        => if the exception end time is later then the regular opening and closing time then look at the regular earliest starting time. If exception end time is like in the middle of the regular working time then look at the earliest opening time.
    TODO: 
    =>Check the exceptions :
        - if exception is open then return the end of the exception 
        - if exception is closed and the time is in the middle of regular working hours then 
        find the earliest possible working time after end of exception.
        - if if exception is closed and the end time is after the regular working hours then return the next day earlies working hour.