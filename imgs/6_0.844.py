d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,1)
d.position_pen(3,0)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)

d.end()
