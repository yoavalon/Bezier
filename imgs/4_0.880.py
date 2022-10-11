d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.N, Length.long)
d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,3)
d.straight_line(Direction.NW, Length.short)
d.position_pen(3,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)

d.end()
