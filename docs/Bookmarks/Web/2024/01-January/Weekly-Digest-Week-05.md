---
- id: 738d76fd-accc-4597-9d22-303e47e5d7be
- id: 95809ce4-8528-4abe-a482-2997d9687d42
- id: 3e4c253e-ad22-4fba-87b8-3864a362fc07
---

%%738d76fd-accc-4597-9d22-303e47e5d7be_start%%

## Preface - LSM in a Week

> [Omnivore](https://omnivore.app/me/preface-lsm-in-a-week-18d5c3adaad) |  [Original](https://skyzh.github.io/mini-lsm/)

### Highlights

> LSM Tree is an append-friendly data structure. [⤴️](https://omnivore.app/me/preface-lsm-in-a-week-18d5c3adaad#cd2c671e-fd0a-4eef-a0e1-fac3aa0013b4) ^cd2c671e

> RB-Tree and B-Tree, all data operations are in-place. That is to say, when you update the value corresponding to the key, the value will be overwritten at its original memory or disk space. But in an LSM Tree, all write operations, i.e., insertions, updates, deletions, are performed in somewhere else. [⤴️](https://omnivore.app/me/preface-lsm-in-a-week-18d5c3adaad#e37285b1-2046-486a-9fee-db5cb753fb18) ^e37285b1

> These operations are applied lazily on disk with a special task called compaction. [⤴️](https://omnivore.app/me/preface-lsm-in-a-week-18d5c3adaad#60e03dc5-16ba-4cca-989b-0a4500aa2589) ^60e03dc5

Immediately, we notice this will not scale well for highly concurrent or order-sensitive transactional data. Not unless the state of writes.updates between two compactions is 

 - preserved in memory for clients
 - is concurrently updated with a consensus. 

Both of these can be thorny issues in production systems. 

---

%%738d76fd-accc-4597-9d22-303e47e5d7be_end%%

%%95809ce4-8528-4abe-a482-2997d9687d42_start%%

## I Just Wanted Emacs to Look Nice — Using 24-Bit Color in Terminals | Chad Austin

> [Omnivore](https://omnivore.app/me/i-just-wanted-emacs-to-look-nice-using-24-bit-color-in-terminals-18d5c2443dd) |  [Original](https://chadaustin.me/2024/01/truecolor-terminal-emacs/)

Thanks to some coworkers and David Wilson’s Emacs from Scratch playlist, I’ve been getting back into Emacs. The community is more vibrant than the last time I looked, and LSP brings modern completion and inline type checking.

### Highlights

> ## Where Did 24-Bit Color Support Come From? [⤴️](https://omnivore.app/me/i-just-wanted-emacs-to-look-nice-using-24-bit-color-in-terminals-18d5c2443dd#6ed8893b-a7b9-4d88-b32d-431b4c820891) ^6ed8893b

A deep dive into terminfo and terminal colors.  
I have been using xterm-256 without realizing what it meant. Now after reading this, I might screw around with my .dot-files and play with tmux-direct and xterm-direct

> Nesting [⤴️](https://omnivore.app/me/i-just-wanted-emacs-to-look-nice-using-24-bit-color-in-terminals-18d5c2443dd#f506c72a-3fc8-42ad-be1a-4d55150de27c) ^f506c72a

This to me is the money shot. Of how a simple terminal on a modern operating system is actually built on decades of abstractions which still try and uphold backward compatibility

---

%%95809ce4-8528-4abe-a482-2997d9687d42_end%%

%%3e4c253e-ad22-4fba-87b8-3864a362fc07_start%%

## COVID Test Data Breach: 1.3 Million Patient Records Exposed Online

> [Omnivore](https://omnivore.app/me/covid-test-data-breach-1-3-million-patient-records-exposed-onlin-18d5c1ce5d9) |  [Original](https://www.vpnmentor.com/news/report-coronalab-breach/)

Cybersecurity Researcher, Jeremiah Fowler, discovered and reported to vpnMentor about a non-password protected database that contained nearly 1.3 million records, which included

### Highlights

> 1.3 million records that included 118,441 certificates, 506,663 appointments, 660,173 testing samples, and a small number of internal application files. The exposed certificates and other documents were all marked with the name and logo of Coronalab.eu. [⤴️](https://omnivore.app/me/covid-test-data-breach-1-3-million-patient-records-exposed-onlin-18d5c1ce5d9#be208e9e-5c94-429d-b040-ce88b92be847) ^be208e9e

ISO certified testing lab and yet a data breach.  
Heard of CISO and their role?  
What are your secturity practices?

> patient’s name, nationality, passport number, and test results, as well as the price, location, and type of test conducted. The database also contained thousands of QR codes and hundreds of.csv files that showed appointment details and many patients’ email addresses. [⤴️](https://omnivore.app/me/covid-test-data-breach-1-3-million-patient-records-exposed-onlin-18d5c1ce5d9#49bc6434-d6f6-4f1a-8ab2-e1ec4714179a) ^49bc6434

PII of the most sensitive nature. Identity Theft potential!

---

%%3e4c253e-ad22-4fba-87b8-3864a362fc07_end%%
