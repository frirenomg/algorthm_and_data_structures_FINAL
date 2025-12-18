console.log("JS CONNECTED");

function runPriority() {
    fetch('/run/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('priority-result').innerText =
                'Executed tasks: ' + data.executed_tasks.join(', ');
        })
        .catch(error => console.error('Error:', error));
}

function runRoundRobin() {
    fetch('/round-robin/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('rr-result').innerText =
                'Execution order: ' + data.round_robin.join(' → ');
        })
        .catch(error => console.error('Error:', error));
}

function runSort() {
    fetch('/sorted/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('sort-result').innerText =
                'Sorted by priority: ' + data.heap_sorted.join(', ');
        })
        .catch(error => console.error('Error:', error));
}
