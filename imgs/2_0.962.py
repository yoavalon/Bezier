d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,0)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.N, Length.long)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
