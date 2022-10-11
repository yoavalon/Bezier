d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(3,0)

d.end()
