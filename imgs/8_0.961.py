d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,1)
d.position_pen(0,3)

d.end()
