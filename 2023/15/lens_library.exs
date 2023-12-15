defmodule Main do
  @moduledoc """
  --- Day 15: Lens Library ---
  https://adventofcode.com/2023/day/15
  """
  def main do
    sum =
      "input.txt"
      |> File.read!()
      |> String.trim()
      |> String.split(",")
      |> Enum.map(&compute_hash/1)
      |> Enum.sum()

    # Run the HASH algorithm on each step in the initialization sequence. What is the sum of the results?
    IO.puts("Part 1: " <> Integer.to_string(sum))
  end

  defp compute_hash(step) do
    step
    |> String.to_charlist()
    |> Enum.reduce(0, fn char, acc -> rem((acc + char) * 17, 256) end)
  end
end

Main.main()
