d = DslBezier()

d.position_pen(1,2)
d.position_pen(2,3)
d.straight_line(Direction.NW, Length.short)
d.position_pen(2,3)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)

d.end()
