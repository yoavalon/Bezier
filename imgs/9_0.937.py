d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.position_pen(3,3)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)

d.end()
