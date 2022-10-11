d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.short)

d.end()
