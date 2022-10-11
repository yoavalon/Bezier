d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,2)

d.end()
