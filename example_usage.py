import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import AgentSpeculativeDecodingOrchestratorClient

def main():
    client = AgentSpeculativeDecodingOrchestratorClient()
    res = client.orchestrate_speculative_run()
    print("=== Agent Speculative Decoding Orchestrator Output ===")
    print(f"Accepted: {res['tokens_accepted_count']}/{res['draft_tokens_proposed']} tokens (Rate: {res['speculative_acceptance_rate']*100}%)")
    print(f"Sequence: '{res['accepted_sequence']}' | First Rejection: '{res['rejected_token']}'")
    print(f"Throughput Speedup: {res['effective_throughput_speedup']} (Latency Cut: {res['latency_reduction_percentage']})")

if __name__ == '__main__':
    main()
