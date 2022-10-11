d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)

d.end()
