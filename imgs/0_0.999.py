d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(2,0)

d.end()
