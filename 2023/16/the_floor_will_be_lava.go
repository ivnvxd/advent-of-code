package main

import (
	"fmt"
	"os"
	"strings"
)

type State struct {
	Y  int
	X  int
	Dy int
	Dx int
}

// Adjust the direction based on the current character
func direction(cur rune, state State) State {
	switch cur {
	case '/':
		state.Dy, state.Dx = -state.Dx, -state.Dy
	case '\\':
		state.Dy, state.Dx = state.Dx, state.Dy
	case '|':
		state.Dy, state.Dx = 1, 0
	case '-':
		state.Dy, state.Dx = 0, 1
	}
	return state
}

// Process the current position and update the stack and energized set
func processPosition(stack *[]State, energized map[[2]int]bool, state State, data []string) {
	if state.Y < 0 || state.Y >= len(data) || state.X < 0 || state.X >= len(data[0]) {
		return
	}

	cur := rune(data[state.Y][state.X])
	if cur == '|' {
		*stack = append(*stack, State{state.Y, state.X, -1, 0})
	} else if cur == '-' {
		*stack = append(*stack, State{state.Y, state.X, 0, -1})
	}

	newState := direction(cur, state)
	*stack = append(*stack, newState)
	energized[[2]int{state.Y, state.X}] = true
}

// Explore the grid and return the count of energized tiles
func traverse(data []string, start State) int {
	stack := []State{start}
	seen := make(map[State]bool)
	energized := make(map[[2]int]bool)

	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if seen[current] {
			continue
		}
		seen[current] = true

		nextState := State{current.Y + current.Dy, current.X + current.Dx, current.Dy, current.Dx}
		processPosition(&stack, energized, nextState, data)
	}

	return len(energized)
}

// Generate all starting directions for the beam
func getAllDirections(m, n int) []State {
	directions := []State{}
	for y := 0; y < m; y++ {
		directions = append(directions, State{y, -1, 0, 1}, State{y, m, 0, -1})
	}
	for x := 0; x < n; x++ {
		directions = append(directions, State{-1, x, 1, 0}, State{n, x, -1, 0})
	}
	return directions
}

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		return
	}

	data := strings.Split(strings.TrimSpace(string(file)), "\n")

	m, n := len(data), len(data[0])

	part1 := traverse(data, State{0, -1, 0, 1})

	directions := getAllDirections(m, n)
	part2 := 0
	for _, start := range directions {
		energized := traverse(data, start)
		if energized > part2 {
			part2 = energized
		}
	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}
