daily-commits
===============

Just some playing-around, this will post your daily commits to twitter,
simple and easy:

1. Authorize yourself into owler.io with your twitter account.
2. You'll get a user page, say it `owler.io/kecebongsoft/`
3. Add a web hook to your repository (or forked repo), use your use page
   URL such as `owler.io/kecebongsoft`
4. For every 00AM, this thing will post your total number of commits for
   the day to your twitter, along with the repository name & url (if exposed), because
   you can also make them private by using `?private=yes` in the web
   hook url parameter.
5. You can also see the complete history of total commits in
   chronological manner from your user page


For a repo with many contributors, you can add multiple web hooks to
send to multiple dailycommits user such as:

* `owler.io/alex/?username=ax`
* `owler.io/kecebongsoft/?username=cebong`
* `owler.io/moto/?username=catfighter`

Using such parameter, daily-commits for `kecebongsoft` will only counted
when there are commits under the username (such as github username)
`cebong`. You can also identify yourself with `email` parameter.


