Problem

-   Openai keys, anthropic keys, whole bunch of other knick knacks.
-   Google credentials json file.
-   Can't litter them in public dotfiles

Requirements

-   Can work as early as .profile and .bashrc.
-   Should be able to share the same setup across machines.
-   As unixy as possible. This isn't supposed to solve for desktop password
    management and key sharing.

Options

-   Big guns - Hashcorp vault, Azure KMS, yada yada.
-   Some form of password / secret manager.
-   Good old pgp? + something.

Solution Blueprint

-   Install pgp
-   Install mozilla sops
-   Generate a pgp key. side channel it to a secure cloud vault. or into a
    separate non-git folder on your pc.
-   Use this pgp key to Sops encrypt files in place.
-   Commit the files to github. Just a bunch of mubled mess with some structure.
-   ~/.profile will use the key + sops to decrypt the file and immediately
    source it with a pipe. No temp files, no disk writing. straigt to process
    memory.
-   Profit.

Hairy Details

# PGP

It’s security mechanism is that we (i.e. client) use a PUBLIC key from the
receiver (i.e. server) and encode it with a random key (I’m saying nonce but it
could be reused)

This varies from RSA and SSH because the server uses a PUBLIC key to identify
the client.

# Web of trust

Web of trust operates by still using PGP (i.e. encoding with recipient’s public
key) but additionally, we can encrypt/sign the data as our own by signing it
with the client’s private key.

This means the recipient will initially decrypt via our (i.e. client’s) public
key (verifying the source) and then decrypting via their (i.e. server’s) private
key to get the data.

To reiterate, the data we send is twice encrypted source’s private key outer
shell, recipient’s public key inner shell.

https://en.wikipedia.org/wiki/Web_of_trust#Simplified_Explanation

# SOPS

For a PGP setup, development machine must have the same public/private PGP key.
Technically, we only need the public key to write content but for
reading/editing we need the private key.

The production server will have the private key for decryption.

We can share the same PGP key for all services or make it per-service (obviously
1 is easier to maintain).

As an alternative to this sensitive setup, we can use AWS’ KMS which will manage
these public/private keys for us. To access said keys, we can use AWS
credentials and their access control policy.

The benefit of using KMS is it decouples the encryption key from access
credentials. Great job by Mozilla here :100:

# Setting up SOPS with PGP

First, get SOPS installed by following its instructions:

https://github.com/mozilla/sops/tree/0494bc41911bc6e050ddd8a5da2bbb071a79a5b7#up-and-running-in-60-seconds

To delete their PGP key (although you likely don’t need to; GPG is more of a
credential manager):

-   List installed keys via `gpg --list-keys`

```
/home/todd/.gnupg/pubring.gpg
-----------------------------
pub   1024R/07FB1A0A 2015-10-08
uid                  SOPS Functional Tests (https://github.com/mozilla/sops/) <ulfr+sopstests@mozilla.com>
sub   1024R/7CD79CC0 2015-10-08
```

-   Delete desired key via `gpg --delete-keys {{fingerprint}}` and
    `gpg --delete-secret-keys {{fingerprint}}`
    -   In the example above, public fingerprint is `07FB1A0A` and private is
        `7CD79CC0`
-   Verify empty files at `~/.gnupg/pubring.gpg` and `~/.gnupg/secring.gpg`

GPG cheatsheet here: http://irtfweb.ifa.hawaii.edu/~lockhart/gpg/gpg-cs.html

Now that we have SOPS installed, let’s set it up in our repo:

1. Generate a GPG key for the repo
    1. Use `gpg --gen-key`. For configuration, I chose:
        1. Key type: RSA and RSA
        2. Keysize: 2048
        3. Expiration: 0 (never expires, otherwise we will have to re-set up
           configs)
        4. Real name: {{repo}} PGP (e.g. “twolfson.com PGP”)
        5. Email address: {{email}}
        6. Comment: PGP credentials for {{repo}} secrets
        7. Password: Empty password
            - You may use a password but all developers and scripts performing
              decryption will need to know that password
            - This effectively makes the password useless since we are more
              concerned about compromising our secrets than the RSA key
2. Find full fingerprint for keys via `gpg --fingerprint`
    - This will be `740D DBFA...` in `Key fingerprint = 740D DBFA...`
3. Create our file via `sops --pgp '{{full_fingerprint}}' secret.enc.yml`
    - For JSON, we can use a non-YAML extension
    - For future edits of the file, we can use `sops secret.enc.yml` (our PGP
      fingerprint has been stored inside of the file)
4. Extract private key to file via
   `gpg --export-secret-keys --armor {{fingerprint}} > private.rsa`
    - `--armor` exports a human-friendly ASCII format instead of binary
5. Upload private key to our server via
   `rsync private.rsa {{server}}:private.rsa`
6. SSH onto our machine
7. Import private key into `gpg` keychain via `gpg --import private.rsa`
8. During deployment, decrypt `secret.enc.yml` to its plaintext variant via
   `sops --decrypt secret.enc.yml > secret.yml`
9. Run server using plaintext `secret.yml`
