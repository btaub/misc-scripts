#!/bin/sh

osascript -e 'tell application "System Events"
	tell security preferences
		set properties to {require password to wake:true}
	end tell
end tell'
