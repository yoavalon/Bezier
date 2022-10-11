d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,0)
d.curve(Direction.N, Orient.right, Length.short, Radius.low)
d.position_pen(0,3)

d.end()
