d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)

d.end()
