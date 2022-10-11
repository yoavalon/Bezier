d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,1)
d.position_pen(2,0)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
