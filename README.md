
=> Exception shows the time period store or charing station is working or not. 
That's why :
    => If exception is "open" then one can directly look at the end of the exception if the timestamp entered by user is inside this exception. 
        =>return end of exception 
    => If exception is "closed" 
        => Look at the one above exception if there is
            => If the given time is inside the corresponding exception:
                => If the exception is open then return end of the exception.
                => else if exception is closed then:
                    => Check the above exception because it can be between those exceptions. 
                        => If it is not between the above exception check the tenant exception. If it is not inside this exception also then 
                                =>If the given time is inside the corresponding exception:
                                    => If the exception is open then return end of the exception.
                                    => else if exception is closed or out of range then:
                                        => Check if end time of the exception is between regular :
                                            => if given time is not between the exception time or closed :
                                                => You are in the top and you need to check regular working_hours
                                                and check the day of the given time and corresponding hours and minutes etc. 
        => if the exception end time is later then the regular opening and closing time then look at the regular earliest starting time. If exception end time is like in the middle of the regular working time then look at the earliest opening time.
    TODO: 
    =>Check the exceptions :
        - if exception is open then return the end of the exception 
        - if exception is closed and the time is in the middle of regular working hours then 
        find the earliest possible working time after end of exception.
        - if if exception is closed and the end time is after the regular working hours then return the next day earlies working hour.