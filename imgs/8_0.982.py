d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.S, Length.long)

d.end()
