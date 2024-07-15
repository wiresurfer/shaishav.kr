---
tags:
  - topic/engineering
  - topic/git
  - topic/productivity
categories:
  - Engineering
title: Mastering Efficient Git Workflows with Stacked PRs
coverImage: https://i.ytimg.com/vi/Uszj_k0DGsg/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLADafbccSoiXapZJyL3Op71IGC-Vw
ShowToc: true
date: 2024-07-15
---
# Mastering Efficient Git Workflows with Stacked PRs

In the fast-paced world of software development, the speed of your engineering team is often bottlenecked by the efficiency of your Pull Request (PR) merges. As seasoned engineers, it's our responsibility to streamline this process, especially in the context of remote-first organizations, large meta-repos, and the non-negotiable need for thorough code reviews. Today, I'm excited to share a game-changing approach that has revolutionized our team's workflow: Stacked PRs.

<!-- more -->

It's not uncommon to come across discussions like [this where someone is unhappy with PR review times in their org](https://www.reddit.com/r/softwaredevelopment/comments/y7xsp4/is_my_company_slow_at_reviewing_pull_requests/), or [this, where there is data to measure PR review wait times rising in Open source projects](https://levelup.gitconnected.com/how-does-pr-review-wait-time-affect-your-open-source-project-d79bd0af0ea3).

## The PR Predicament: Big, Bloated, and Bottlenecked

Before we dive into the solution, let's dissect the problem that plagues many engineering teams.

### The Burden of Big PRs

According to a study by GitClear[^1], senior developers spend an average of 4 hours per day reviewing code, with larger PRs taking disproportionately more time. This statistic is alarming, especially when we consider the cognitive load that comes with reviewing extensive changes.

![PR Size vs. Review Time](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*TJzbO53-CUN0FO7ZwWNsGA.jpeg)

Big PRs are notoriously difficult to make sense of, primarily because they often violate the KISS (Keep It Simple, Stupid) principle. Google's engineering guidelines suggest that a "big" PR contains more than 400 lines of changes[^2]. However, the real issue isn't just the size, but the complexity that arises from mixing different types of changes:

- **Chores**: Routine maintenance tasks
- **Features**: New functionalities
- **Hotfixes**: Urgent bug fixes
- **Bugfixes**: Non-urgent corrections
- **Improvements**: Enhancements to existing features

When a single PR combines these various change types, it becomes a Herculean task for reviewers to maintain context and ensure quality.

> "The responsibility of a PR reviewer is directly proportional to the clarity and manageability of the changes they're reviewing."

This axiom highlights a critical issue: PR reviewers can only be held accountable if they fully understand what they're signing off on. Large, complex PRs often lead to delayed reviews or superficial "code-read" approvals, as the effort required to pull, run, and verify extensive changes becomes prohibitive.

### The Meta-Repo Maze

The rise of meta-repositories has added another layer of complexity to the PR review process. These repos often include:

- Infrastructure-as-code
- Documentation-as-code
- Client-side components
- Microservice backends
- Multiple programming languages

In this context, code ownership becomes fragmented, and when a PR touches multiple components, it dilutes responsibility among various owners. This fragmentation often results in a focus on the most changed component, neglecting equally important but less modified parts.

### The CI/CD Conundrum

Complex PRs also pose challenges for Continuous Integration and Continuous Deployment (CI/CD) pipelines. It becomes increasingly difficult to:

- Write workflows that accurately test all affected components
- Ensure that Quality Assurance (QA) processes provide a robust safety net
- Maintain velocity without compromising on thorough testing

## Stacked PRs: A Paradigm Shift

Enter Stacked PRs – a workflow that addresses these challenges head-on by breaking down large changes into smaller, more manageable pieces.

![Stacked PRs Visualization](Assets/media/Efficient%20Git%20Workflow%20with%20Stacked%20PRs/Efficient%20Git%20Workflow%20with%20Stacked%20PRs-image-20231228203144373.png)

### The Core Idea

Stacked PRs involve creating a series of dependent PRs, each building upon the changes of the previous one. This method allows for:

1. **Incremental Reviews**: Reviewers can focus on smaller, more digestible chunks of code.
2. **Parallel Work**: Developers can continue working on subsequent changes while waiting for reviews.
3. **Easier Rollbacks**: If issues are found, it's simpler to revert or fix specific parts of the change.

### Benefits of Stacked PRs

1. **Enhanced Review Process**: Smaller, focused PRs are easier to review, reducing the time spent on each PR and increasing the quality of the reviews.
2. **Improved Accountability**: With smaller PRs, reviewers can better understand and take responsibility for the changes they approve.
3. **Streamlined CI/CD**: CI/CD pipelines can process smaller changes more efficiently, providing quicker feedback and reducing the risk of integration issues.

### Evidence of Efficacy

1. **FAANG Adoption**: Companies like Facebook and Google have long used variations of this approach, contributing to their ability to maintain high-velocity development in large codebases[^3].

2. **Open Source Success**: Popular open-source projects like Linux kernel development utilize a similar concept with patch series, enabling rapid iteration and thorough review processes[^4].

3. **Improved Metrics**: Teams adopting stacked PRs often report:
   - Reduced time-to-merge for complex features
   - Increased reviewer engagement
   - Higher code quality due to more focused reviews

## Implementing Stacked PRs: A Practical Playbook

Adopting a stacked PR workflow involves several key components and considerations. Let's break down the solution into its core aspects before diving into the implementation checklist.

### Key Aspects of Stacked PRs

1. **Branch Management**: 
   Stacked PRs require a disciplined approach to branch creation and management. Each "stack" typically consists of a series of branches, each building upon the previous one.

2. **Tooling**: 
   While stacked PRs can be managed manually, specialized tools can significantly streamline the process. These tools help with branch creation, rebasing, and PR management.

3. **Code Review Process**: 
   Reviewers need to understand the context of each PR within the stack and review them in order. This often requires a shift in the review mindset.

4. **CI/CD Integration**: 
   Continuous Integration and Deployment pipelines need to be adapted to handle interdependent PRs effectively.

5. **Team Communication**: 
   Clear communication about the status and dependencies of stacked PRs is crucial for smooth collaboration.

### Tools for Stacked PRs

Several tools have emerged to support stacked PR workflows:

1. **Graphite**: A comprehensive tool designed specifically for managing stacked PRs, offering features like automatic rebasing and dependency tracking[^5].

2. **gh-stack**: A GitHub CLI extension that helps manage PR stacks directly from the command line[^6].

3. **spr (Stacked Pull Requests)**: A tool that integrates with GitHub to facilitate the creation and management of stacked PRs[^7].

4. **Stacked Pull Requests by Aviator**: A GitHub app that provides a visual interface for managing PR stacks[^8].

5. **git-branchless**: An experimental tool inspired by the Linux kernel development process, offering advanced history editing and stack management features[^9].

Now, let's dive into the implementation checklist:

## Implementation Checklist

### One-time Setup

- [ ] Choose a stacked PR management tool
    - [ ] Evaluate options like Graphite, gh-stack, or spr based on your team's needs
    - [ ] Consider factors like GitHub integration, ease of use, and feature set

- [ ] Update team Git workflow documentation
	- [ ] Document the chosen stacked PR process
	- [ ] Create guidelines for when to use stacked PRs vs. single PRs

- [ ] Configure CI/CD pipelines for stacked PRs
	- [ ] Set up dependency awareness in your CI system
	- [ ] Ensure tests run on the merged state of stacked PRs

- [ ] Establish branch naming conventions
	- [ ] Create a system that clearly indicates the order and relationship of branches in a stack
  	- For example: `feature/base-branch`, `feature/base-branch-part2`, etc.

### Recurring Tasks

#### Onboarding Engineers
- [ ] Develop training materials for the stacked PR workflow
	- [ ] Create video tutorials or written guides
	- [ ] Include hands-on exercises for practicing the workflow

- [ ] Pair experienced developers with newcomers
	- [ ] Schedule pairing sessions for creating and managing stacked PRs
	- [ ] Encourage questions and provide real-time guidance

- [ ] Conduct regular refresher sessions
	- [ ] Address common pitfalls and share best practices
	- [ ] Showcase successful examples from the team's work

#### Bootstrapping Projects
- [ ] Create PR description templates
	- [ ] Include sections for describing the PR's place in the stack
	- [ ] Prompt for information on dependencies and testing considerations

- [ ] Set up project-specific GitHub labels
	- [ ] Create labels like "stack-base", "stack-middle", "stack-top" for easy identification

- [ ] Configure branch protection rules
	- [ ] Ensure base branches of stacks are protected
	- [ ] Set up required reviews and status checks appropriate for stacked PRs

#### CI/CD/QA/DevOps
- [ ] Implement stack-aware CI checks
	- [ ] Develop scripts to validate the entire stack before allowing merges
	- [ ] Set up checks to ensure PRs are not merged out of order

- [ ] Create automated dependency tracking
	- [ ] Use GitHub Actions or similar tools to update PR descriptions with stack info
	- [ ] Automatically link related PRs in comments or labels

- [ ] Configure notification systems
	- [ ] Set up Slack/Teams integrations to alert on stack updates
	- [ ] Create custom notifications for reviewers when dependent PRs change

- [ ] Develop metrics and monitoring
	- [ ] Track metrics like time-to-merge for stacked vs. traditional PRs
	- [ ] Monitor the frequency and size of stacks to identify trends and improvement areas

#### Code Review Process
- [ ] Update code review guidelines
	- [ ] Provide instructions on how to review stacked PRs effectively
	- [ ] Emphasize the importance of reviewing in stack order

- [ ] Create a review checklist specific to stacked PRs
	- [ ] Include items like "Verified changes in context of previous stack PRs"
	- [ ] Prompt reviewers to consider the impact on subsequent PRs in the stack

- [ ] Set up review assignment automation
	- [ ]Configure tools to automatically assign the same reviewers to all PRs in a stack
	- [ ]Ensure primary reviewers are consistent across the stack for context retention

By following this expanded playbook, teams can more effectively implement and maintain a stacked PR workflow. Remember, the key to success is continuous improvement – regularly solicit feedback from your team and iterate on the process to find what works best in your specific context.

## Embracing the Stacked PR Future

Adopting Stacked PRs isn't just about changing a workflow; it's about fostering a culture of incremental improvement and focused collaboration. By breaking down large changes into manageable, reviewable pieces, we not only accelerate our development process but also enhance the quality of our codebase.

> "The best code is not just written well, but reviewed well. Stacked PRs make great reviews not just possible, but inevitable."

As we continue to refine this approach, I'm eager to hear your thoughts and experiences. Have you implemented Stacked PRs in your team? What challenges did you face, and what unexpected benefits did you discover?

Let's continue this conversation and push the boundaries of efficient software development together. Share your insights, suggestions, or questions with me on Twitter [@wiresurfer](https://twitter.com/wiresurfer). Together, we can stack our way to software engineering excellence!






## Further Reading
- [How to visualize stacked git branches | by Greg Foster | Medium](https://gregmfoster.medium.com/how-to-visualize-stacked-git-branches-e10827242304)
- [Stacked pull requests: make code reviews faster, easier, and more effective - Dr. McKayla](https://www.michaelagreiler.com/stacked-pull-requests/)
- [Stacked Diffs Versus Pull Requests | Jackson Gabbard's Blog](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/)
- [Stacked Pull Requests · GitHub Marketplace · GitHub](https://github.com/marketplace/stacked-pull-requests)
- [How to Handle Stacked Pull Requests on GitHub | PSPDFKit](https://pspdfkit.com/blog/2021/how-to-handle-stacked-pull-requests-on-github/)
- [Stacked Pull Requests](https://matt-rickard.com/stacked-pull-requests)
- [A Better Model for Stacked (GitHub) Pull Requests • Timothy Andrew](https://timothya.com/blog/git-stack/)


---


[^1]: [GitClear Study on Code Review Time](https://www.gitclear.com/blog/new_data_reveals_the_hidden_costs_of_context_switching_and_meetings_for_developers) This study provides insights into developer time allocation, highlighting the significant portion dedicated to code reviews.

[^2]: [Google's Engineering Practices documentation](https://google.github.io/eng-practices/review/developer/small-cls.html) Google's guidelines on code review best practices, including recommendations on PR size.

[^3]: [Facebook's Phabricator and Stacked Diffs](https://kurtisnusbaum.medium.com/stacked-diffs-keeping-phabricator-diffs-small-d9964f4dcfa6) An insider look at how Facebook uses stacked diffs to manage large-scale development.

[^4]: [Linux Kernel Development Process](https://www.kernel.org/doc/html/latest/process/2.Process.html#how-patches-get-into-the-kernel) The Linux kernel's patch submission process, which inspired many modern stacked PR workflows.

[^5]: [Graphite - How the fastest developers ship code](https://graphite.dev/)

[^6]: [GitHub - timothyandrew/gh-stack: Manage PR stacks/chains on Github](https://github.com/timothyandrew/gh-stack/)

[^7]: [spr | Stacked Pull Requests on GitHub](https://ejoffe.github.io/spr/)

[^8]: [Stacked PRs](https://www.aviator.co/stacked-prs)

[^9]: [GitHub - arxanas/git-branchless: High-velocity, monorepo-scale workflow for Git](https://github.com/arxanas/git-branchless)

<!---

### Big PRs
- %% statistics about time spent by senior devs in PR reviews. short 2-3lines. quote with reference+statistics from mid sized startups %%
- %% why big PRs are harder to make sense of . general intro - 2 lines.  %%
	- %% define BIG PR.  400line changes as per google's guidelines.   short , 2 lines %%
	- %% types of PR changes. chore vs feature, vs hotfix vs bugfix vs improvement.  refer to conventional commits.  Any PR mixing these changes into one single Big PR is trying to do too much. violates KISS.  elaborate with 3-4lines %%
- %% The need to make a PR reviewer responsible/accountable for PRs they accept. can't expect this, if PRs aren't easy to understand/work with %%
	- %% where does the buck stop when changes cause issues.  PR reviewers will happily take responsibility, if they knew what they were signing off on.  %%
	- %% people delay proper reviews, or only do code-read reviews if the changes are large.  smaller changes are easier to pull, run and verify %%

### Meta-repos and PR Reviews
- %% Rise of meta-repos. infra as code, documentation as code, client side components, microservice backends, multiple languages %%
- %% code ownership models and multiple owners for large PR dilutes responsibility %%
- %% mixing multiple component changes into one PR always puts the focus on the most changed component. ideally should have focus on ALL components. non-negotiable for quality %%
### PRs with separation of concern. 
- %% Difficulty building tools for CI/CD when PRs get more complex %%
	- %% easier to write workflows and CI for small PRs which are isolated to components. QA needs this to guarantee tests provide a safety net for velocity. 3-4 lines %%


## Talk about the Core Idea of the Solution


## Evidence about the Solution Approach


## Solution Playbook 


## Call to Action


## Further Reading
6. [GitHub - timothyandrew/gh-stack: Manage PR stacks/chains on Github](https://github.com/timothyandrew/gh-stack/)
7. [Graphite - How the fastest developers ship code | Graphite](https://graphite.dev/)
8. [spr | Stacked Pull Requests on GitHub](https://ejoffe.github.io/spr/)
9. [Stacked PRs](https://www.aviator.co/stacked-prs)
10. [Stacked Pull Requests · GitHub Marketplace · GitHub](https://github.com/marketplace/stacked-pull-requests)
11. [How to Handle Stacked Pull Requests on GitHub | PSPDFKit](https://pspdfkit.com/blog/2021/how-to-handle-stacked-pull-requests-on-github/)
12. [Stacked Pull Requests](https://matt-rickard.com/stacked-pull-requests)
13. [A Better Model for Stacked (GitHub) Pull Requests • Timothy Andrew](https://timothya.com/blog/git-stack/)
14. Experimental Ideas as used in Linux Kernel
	1. [GitHub - arxanas/git-branchless: High-velocity, monorepo-scale workflow for Git](https://github.com/arxanas/git-branchless)
-->