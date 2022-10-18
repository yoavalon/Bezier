d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.long)

d.end()
