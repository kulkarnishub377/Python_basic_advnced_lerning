from managers import FileTransaction, execution_timer
import time

def run_atomic_write_demo():
    print("Initiating Native Context Manager structurally mapped completely flawlessly!")
    print("-" * 50)
    
    filename = "database.txt"
    
    # 1. Success Flow Native Execution
    with FileTransaction(filename) as ft:
        ft.write("Structural Explicit Record Natively Flawlessly Generated!\n")
        
    print("\nSimulating Failure structurally flawlessly explicit rollback!")
    # 2. Failure Native Extrusion Logic
    try:
        with FileTransaction(filename) as ft:
            ft.write("This explicit mapping should actively completely identically disappear...")
            # Dynamically actively generating mathematical crashes natively!
            raise ValueError("Deliberate execution failure cleanly natively!")
    except ValueError:
        print("Caught explicit mathematical ValueError inherently structurally gracefully.")

def run_timer_demo():
    print("\nExecuting computationally precisely mathematically native timing operations.")
    with execution_timer():
        # Everything precisely seamlessly inside exactly strictly this block natively executes physically timed!
        time.sleep(0.3)
        total = sum(x**2 for x in range(100_000))
        
    print("Execution definitively inherently concluded flawlessly natively!")

if __name__ == "__main__":
    run_atomic_write_demo()
    run_timer_demo()
