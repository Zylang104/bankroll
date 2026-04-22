local ui = game:GetService("UserInputService")
local ismobile = ui.TouchEnabled and not ui.KeyboardEnabled
if ismobile then
    loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/94e4645e50be134161403e01dbc7b30fe16371d945b91774183154e3f57c8ad9/download"))()
else
    loadstring(game:HttpGet("https://api.jnkie.com/api/v1/luascripts/public/93e2ea1275134d92a1c27001e45b45914e84b69b773f38b086a5c924cafe0425/download"))()
end
