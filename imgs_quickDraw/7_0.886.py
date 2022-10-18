d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,3)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.W, Length.long)

d.end()
