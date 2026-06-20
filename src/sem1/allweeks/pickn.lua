math.randomseed(os.time() + os.clock())

local n = 10
local m = 50

local range = {}
for i = 1, m do
	range[i] = i
end

for i = m, 2, -1 do
	local j = math.random(1, i)
	range[i], range[j] = range[j], range[i]
end

print("Picked " .. n .. " from 1.." .. m .. ":")
for i = 1, n do
	print(range[i])
end
