d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NW, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.long)

d.end()
