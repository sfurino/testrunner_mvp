# testrunner


**testrunner** is the execution engine for running automated tests.

It is designed to be installed *everywhere* in your environment, and thus lives under some design constraints:

* It's just an executable - use something else (ansible, salt, magic beans) to execute it at scale. 
* It's a single file - doesn't care if it's in /usr/bin, ~/bin, or your sock drawer.
* It has no dependencies - it works on a minimal-install of RHEL7

The last constraint is the reason we didn't use modern things like python3, requests, and the like.  It's also why there's currently a bare-bones fakeout of RFC7578 in there.



## Using testrunner


You will need some ingredients to make a tasty soup.

This repo *does* contain demo ingredients, but you should not use them beyond getting an idea of what testrunner can do.  Think of them like the plastic turkey on the table at your local furniture store.

The three ingredients are:

* trserver - distributes tests

   This is probably a http server, and can serve read-only.  This is probably where the .tr.idx files are made too.  
   But unlike the demo version, you probably will want to update the indexes without restarting the server, and even get into multi-user pulls from their source repos in response to webhooks, locked tests and the like.  And have something that can handle a few users at a time.

* resultserver - receive the results of tests

   This is probably a http server (maybe the same one?) that can accept uploaded result files.  The RFC4122 uuid's that testrunner uses should be unique - so you should be able to accept only files that don't exist, and limit the file size / per-host frequency based on your environment's use case.

* tests 

  Ahhh.  Here's the good stuff.  Of course you need those.  Tests can be as simple or as complex as you'd like.  Some very simple examples are included in the demo-testroot.  
  Don't think of small tests as having less value - we have seen some teams which have hundreds of <20 line tests in their strategies - while others carry a specific JVM and the SPECjbb test suite in a test.

## tbc



