d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,0)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)

d.end()
