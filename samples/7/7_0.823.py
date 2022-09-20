d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
