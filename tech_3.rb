def balanced(s)
  stack = []
  close_mapping = {')' => '(', '}' => '{', ']' => '['}
  s.each_char do |char|
    if close_mapping.values.include?(char)
      stack << char
    elsif close_mapping.key?(char)
      if stack.empty? || stack[-1] != close_mapping[char]
        return false
      else
        stack.pop()
      end
    end
  end
  return stack.empty?
end

# puts balanced('')
# puts balanced('(({}))')
# puts balanced('([{}[]])')
# puts balanced('(()')
# puts balanced('(]')
# puts balanced('(()){[[)]}')
# puts balanced('(((')
# puts balanced(']]]]')

def p_triangle(n)
  return [1] if n == 0

  prev_level = p_triangle(n-1)
  curr_level = Array.new(n+1)
  (0...n+1).each do |i|
    left = i-1 == -1 ? 0 : prev_level[i-1]
    right = i > n-1 ? 0 : prev_level[i]
    curr_level[i] = left + right
  end
  return curr_level
end

p p_triangle(0)
p p_triangle(1)
p p_triangle(2)
p p_triangle(4)




