d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,0)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(3,2)
d.straight_line(Direction.N, Length.short)
d.position_pen(3,1)

d.end()
