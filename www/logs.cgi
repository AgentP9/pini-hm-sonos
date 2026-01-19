#!/usr/bin/env tclsh
source [file join [file dirname [info script]] sonos2inc.tcl] ;# Include-File

# Parse query parameters
parseQuery

# Check if this is a request for the HTML page or log content
if {[info exists args(tail)] || [info exists args(getlogs)]} {
    # Return log content
    puts "Content-type:text/plain\n"
    
    # Get the log file path
    set logfile [file join [file dirname [info script]] $flog]
    
    # Check if we're getting full log or just tail
    set lines 100
    set tail 0
    if {[info exists args(tail)]} {
        set tail 1
        if {[info exists args(lines)] && [string is integer $args(lines)]} {
            set lines $args(lines)
        }
    }
    
    # Read the log file
    set content ""
    if {[file exists $logfile]} {
        if {$tail} {
            # Get last N lines
            catch {
                set fd [open "| tail -n $lines $logfile" r]
                fconfigure $fd -encoding utf-8
                set content [read $fd]
                close $fd
            }
        } else {
            # Get entire file
            catch {
                set fd [open $logfile r]
                fconfigure $fd -encoding utf-8
                set content [read $fd]
                close $fd
            }
        }
    }
    
    # Output the content
    if {$content == ""} {
        puts "No log entries found."
    } else {
        puts $content
    }
} else {
    # Return HTML page
    set content [loadFile logs.html]
    set zone ""
    if [info exists args(zone)] {
        if {$args(zone) != "" && $args(zone) != "fehlt"} { set zone "?zone=$args(zone)"}
    }
    regsub -all {<%zone%>} $content  $zone content ;#" %>
    puts "Content-type:text/html\n"
    puts $content
}
