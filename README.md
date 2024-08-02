# First-Come-First-Served-FCFS-Scheduling-Algorithm
This repository contains an implementation of the First-Come, First-Served (FCFS) scheduling algorithm in Python. FCFS is the simplest type of CPU scheduling algorithm, where processes are executed in the order they arrive in the ready queue

## Overview
The First-Come, First-Served (FCFS) scheduling algorithm is one of the simplest CPU scheduling algorithms used in operating systems. In FCFS, the process that arrives first in the ready queue is executed first. It is a non-preemptive algorithm, meaning that once a process starts its execution, it runs to completion without interruption.

## How It Works
- **Queue Order:** Processes are executed in the order they arrive in the ready queue. The first process in the queue is given control of the CPU, and it runs to completion before the next process starts.
- **Non-Preemptive:** Once a process begins execution, it will not be interrupted by any other process, regardless of their arrival time or burst time.
- **Simplicity:** The algorithm's simplicity lies in its straightforward implementation and the fact that it does not require complex decision-making.

## Advantages
- **Simplicity:** FCFS is easy to implement and understand. It operates on a simple "first-come, first-served" basis, similar to a queue in real life.
- **Fairness in Order:** Every process gets a chance to execute in the exact order they arrive, ensuring a fair and predictable execution pattern.
- **Low Overhead:** There are no context switches required during the execution of a process, minimizing CPU overhead.

## Disadvantages
- **Convoy Effect:** A long process can delay all subsequent processes, leading to what is known as the "convoy effect," where shorter processes have to wait for longer ones to finish.
- **Poor Response Time:** Processes arriving later, even if short, will experience longer waiting times, leading to potentially poor response times.
- **Not Suitable for Interactive Systems:** FCFS is not ideal for systems where quick response times are needed, as it may lead to unacceptable delays for shorter or more urgent tasks.

## Usage
To run the FCFS scheduling simulation, clone the repository and execute the Python script:

```bash
git clone https://github.com/yourusername/fcfs-scheduling.git
cd fcfs-scheduling
python fcfs.py
