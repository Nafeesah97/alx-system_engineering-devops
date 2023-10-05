#!/usr/bin/env ruby
sender = ARGV[0].scan(/\[from:(\w+)\]/).join(",")
receiver = ARGV[0].scan(/\[to:(\+\d+)\]/).join(",")
flags = ARGV[0].scan(/\[flags:(\w+)\]/).join(",")

puts "#{sender},#{receiver},#{flags}"
