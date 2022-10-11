d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.position_pen(1,0)

d.end()
