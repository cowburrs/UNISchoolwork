math.randomseed(os.time())

local function pick_random(n, min, max)
	local results = {}
	for i = 1, n do
		results[i] = math.random(min, max)
	end
	return results
end

local n = 5
local min = 1
local max = 50

local numbers = pick_random(n, min, max)

print(string.format("Picking %d random numbers from [%d, %d]:", n, min, max))
for i, v in ipairs(numbers) do
	print(string.format("  [%d] %d", i, v))
end
